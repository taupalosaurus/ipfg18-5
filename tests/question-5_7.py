test = {
  'name': 'question 5.7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(calc_material_velocity) == types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(param) # wrong number of argument
          3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import types; import inspect; param = inspect.signature(calc_material_velocity).parameters',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(calc_material_velocity(*_m1), _v1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(calc_material_velocity(*_m2), _v2)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(calc_material_velocity(*_m3), _v3)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sanity_check(-6.85, 20.9, 2580)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sanity_check(6.85, -20.9, 2580)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sanity_check(-6.85, 20.9, -2580)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': """
_m1 = (44, 38, 2650)
_v1 = (6.039700938074968, 4.074772826171499)
_m2 = (6.85, 20.9, 2580)
_v2 = (3.411865600135066, 1.6294289673655376)
_m3 = (0, 2.29, 1000)
_v3 = (1.5132745950421556, 0.0)
import numpy as np
def sanity_check(arg1, arg2, arg3):
    try:
        calc_material_velocity(arg1, arg2, arg3)
    except ValueError:
        return True
    return False
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
