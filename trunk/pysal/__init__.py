import cg
import core

import pysal.core.FileIO # Load IO metaclass
import pysal.core._FileIO # Load IO inheritors

#Assign pysal.open to dispatcher

open = pysal.core.FileIO.FileIO
