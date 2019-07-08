import atexit
import shutil
import tempfile

STANSUMMARY_STATS = [
    'Mean',
    'MCSE',
    'StdDev',
    '5%',
    '50%',
    '95%',
    'N_Eff',
    'N_Eff/s',
    'R_hat',
]

TMPDIR = tempfile.mkdtemp()


def cleanup_tmpdir():
    print('deleting tmpfiles dir: {}'.format(TMPDIR))
    shutil.rmtree(TMPDIR, ignore_errors=True)
    print('done')


atexit.register(cleanup_tmpdir)

from .cmds import compile_model, sample, summary, diagnose, get_drawset
from .cmds import save_csvfiles
from .utils import set_cmdstan_path, cmdstan_path, set_make_env, jsondump, rdump
from .lib import Model, RunSet
from .__version__ import __version__
