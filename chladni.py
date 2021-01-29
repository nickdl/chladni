import numpy as np
from PIL import Image

SIZE = (1080, 1080)
# SIZE = (1080, 1920)
DENSITY = .7
ISOLATION = 3
NOISE = .0001

# n, m = 4, 8
n, m = 1, 12
p, q = n, m
a, b = SIZE
C, D = -1., 1.
x, y = np.ogrid[:SIZE[0], :SIZE[1]]
c = np.random.random(4) * 360 * NOISE
pattern = C * np.cos(m * np.pi * x / a + c[0]) * np.cos(n * np.pi * y / b + c[1]) + \
          D * np.cos(p * np.pi * x / a + c[2]) * np.cos(q * np.pi * y / b + c[3])
pattern = np.abs(pattern)
pattern = np.interp(pattern, (pattern.min(), pattern.max()), (0., 1.))
pattern = 1 - pattern
pattern = np.power(pattern, ISOLATION)
pattern = np.random.binomial(n=1, p=pattern * DENSITY, size=pattern.shape) * pattern
image = Image.fromarray(np.uint8(pattern * 255), mode='L')
image.show()
path = 'n:%s-m:%s.png' % (n, m)
# image.save(path, optimize=True)
