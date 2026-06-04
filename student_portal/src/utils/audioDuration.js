/**
 * Returns duration in whole seconds for a File/Blob. WebM from MediaRecorder
 * often lacks duration in HTML <audio> metadata; decodeAudioData is more reliable.
 */
export async function getAudioDurationSeconds(file) {
  if (!file) return null;

  try {
    const ctx = new AudioContext();
    const arrayBuffer = await file.arrayBuffer();
    const audioBuffer = await ctx.decodeAudioData(arrayBuffer.slice(0));
    await ctx.close();
    if (Number.isFinite(audioBuffer.duration) && audioBuffer.duration > 0) {
      return Math.round(audioBuffer.duration);
    }
  } catch {
    /* try <audio> metadata next */
  }

  return new Promise((resolve) => {
    const url = URL.createObjectURL(file);
    const audio = new Audio();
    audio.preload = 'metadata';

    const finish = (value) => {
      URL.revokeObjectURL(url);
      resolve(value);
    };

    audio.addEventListener(
      'loadedmetadata',
      () => {
        const d = audio.duration;
        if (Number.isFinite(d) && d > 0 && d !== Infinity) {
          finish(Math.round(d));
        } else {
          finish(null);
        }
      },
      { once: true }
    );
    audio.addEventListener('error', () => finish(null), { once: true });
    audio.src = url;
  });
}
