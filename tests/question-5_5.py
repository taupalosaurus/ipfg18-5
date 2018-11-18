test = {
  'name': 'question 5.5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(isInt) == types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(param) # wrong number of argument
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import types; import inspect; param = inspect.signature(isInt).parameters',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> isInt(random_int)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isInt(random_float)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isInt(random_string)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isInt(random_int_string)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isInt(random_float_string)
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import random
import string
random_int = random.randint(1,100)
random_float = random.random()
random_string = ''.join([random.choice(string.ascii_letters) for i in range(5)])
random_int_string = ''.join([random.choice(string.digits) for i in range(3)])
random_float_string = '.'.join([random.choice(string.digits) for i in range(2)])
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
