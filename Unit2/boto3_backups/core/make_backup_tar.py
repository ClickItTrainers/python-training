import os
import tarfile
from core.local_logging import info
from core.config import CURRENT_DIRECTORY
from os import remove

class MakeBackups:
    """Class to make backups in tar.gz format
    Args:
        output_filename: The name of the file to br created as tar.gz
        source_dir: The file/directory to make the tar.gz file
    """
    def __init__(self, output_filename: str, source_dir: str):
        self.output_filename = output_filename
        self.source_dir = source_dir
        self.targz_file_path = ''

    def return_backup_path(self) -> str:
        targz_path = str(CURRENT_DIRECTORY).split('/')[:-1]
        targz_path = "/".join(targz_path)
        self.targz_file_path = f"{targz_path}/{os.path.basename(self.output_filename)}"

        return self.targz_file_path

    def create_tar_file(self) -> str:
        """Create a tar.gz file for given file"""
        info(f'Creating tar file for {os.path.basename(self.source_dir)}')
        with tarfile.open(self.output_filename, "w:gz") as tar:
            tar.add(self.source_dir, arcname=os.path.basename(self.source_dir))

        return self.return_backup_path()

    def delete_file(self):
        info(f"Removing file {self.return_backup_path()}")
        remove(self.return_backup_path())
    