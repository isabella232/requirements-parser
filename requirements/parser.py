import os
import warnings

from .requirement import Requirement


def parse(reqstr, current_path = "", file_system = None):
    """
    Parse a requirements file into a list of Requirements

    See: pip/req.py:parse_requirements()

    :param reqstr: a string or file like object containing requirements
    :returns: a *generator* of Requirement objects
    """
    filename = getattr(reqstr, 'name', None)
    try:
        # Python 2.x compatibility
        if not isinstance(reqstr, basestring):
            reqstr = reqstr.read()
            current_path = filename
    except NameError:
        # Python 3.x only
        if not isinstance(reqstr, str):
            reqstr = reqstr.read()
            current_path = filename

    for line in reqstr.splitlines():
        line = line.strip()
        if line == '':
            continue
        elif not line or line.startswith('#'):
            # comments are lines that start with # only
            continue
        elif line.startswith('-r') or line.startswith('--requirement'):
            _, new_filename = line.split()
            new_file_path = os.path.join(os.path.dirname(current_path), 
                                        new_filename)

            if not file_system:
                file_system = LocalFileSystem()

            new_req_file = file_system.open(new_file_path)
            
            for requirement in parse(new_req_file, new_file_path, file_system):
                yield requirement

        elif line.startswith('-f') or line.startswith('--find-links') or \
                line.startswith('-i') or line.startswith('--index-url') or \
                line.startswith('--extra-index-url') or \
                line.startswith('--no-index'):
            warnings.warn('Private repos not supported. Skipping.')
            continue
        elif line.startswith('-Z') or line.startswith('--always-unzip'):
            warnings.warn('Unused option --always-unzip. Skipping.')
            continue
        else:
            yield Requirement.parse(line)

class LocalFileSystem:
    def open(self, path):
        with open(path, "r") as f:
            return f.read()