test = {
  'name': 'question 5.8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(wave_velocities)==np.ndarray 
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(wave_velocities, [15.7691, -1., 6.116735, -1., 5.193774, -1.])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
