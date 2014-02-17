# FEM stuff to move/split to common.
from sfepy.discrete.fem.region import Region
from sfepy.discrete.fem.fields_base import Field, VolumeField, SurfaceField

from functions import Functions, Function
from conditions import Conditions
from variables import Variables, Variable, FieldVariable, create_adof_conns
from materials import Materials, Material
from equations import Equations, Equation
from integrals import Integrals, Integral
from state import State
from problem import ProblemDefinition
from evaluate import assemble_by_blocks
