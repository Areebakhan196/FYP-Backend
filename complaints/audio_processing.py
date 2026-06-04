import os
import logging

logger = logging.getLogger('complaints')

# Formats we keep as-is (browser recordings). No pydub import required.
_SKIP_TRANSCODE_EXTENSIONS = ('.webm', '.opus', '.m4a', '.mp4', '.ogg')


def process_audio(file_path):
    """
    Optional post-processing. Browser recordings (webm/m4a/ogg) are left as-is
    so quality is not reduced by re-encoding.
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext in _SKIP_TRANSCODE_EXTENSIONS:
        logger.info("Skipping transcoding for %s to preserve original quality.", ext)
        return file_path
    try:
        # Lazy import: pydub pulls in audioop (removed in Python 3.13+).
        from pydub import AudioSegment

        audio = AudioSegment.from_file(file_path)
        base_name = os.path.splitext(file_path)[0]
        output_path = f"{base_name}_processed.mp3"
        
        # Export without tags to ensure anonymity
        audio.export(output_path, format="mp3", tags={})
        
        logger.info(f"Audio processed successfully: {output_path}")
        return output_path
    except Exception as e:
        logger.error(f"Audio processing failed: {str(e)}")
        return file_path
