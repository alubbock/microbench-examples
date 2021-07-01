import tempfile
import os

def test_microbench_slurm():
    with tempfile.TemporaryDirectory() as td:
        # Set working directory to temp dir
        os.chdir(td)

        # Execute the script via import
        import microbench_slurm
