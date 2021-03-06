__all__ = []

# The following pattern is used below for importing sub-modules:
#
# 1. "from foo import *".  This imports all the names from foo.__all__ into
#    this module. But, this does not put those names into the __all__ of
#    this module. This enables "from sympy.physics.mechanics import kinematics" to
#    work.
# 2. "import foo; __all__.extend(foo.__all__)". This adds all the names in
#    foo.__all__ to the __all__ of this module. The names in __all__
#    determine which names are imported when
#    "from sympy.physics.mechanics import *" is done.

from . import kane
from .kane import *
__all__.extend(kane.__all__)

from . import rigidbody
from .rigidbody import *
__all__.extend(rigidbody.__all__)

from . import functions
from .functions import *
__all__.extend(functions.__all__)

from . import particle
from .particle import *
__all__.extend(particle.__all__)

from . import point
from .point import *
__all__.extend(point.__all__)

from . import essential
from .essential import *
__all__.extend(essential.__all__)

from . import lagrange
from .lagrange import *
__all__.extend(lagrange.__all__)
