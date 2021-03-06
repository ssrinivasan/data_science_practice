import matplotlib.pyplot as MPL
import numpy as NP
import matplotlib.cm as cm
#from scipy import misc as MSC
#import matplotlib.image as MPI

class CheckerBoard:
    def __init__(self, r_pixel=800, c_pixel=800, num_block=8):        
        self.r_pixel = r_pixel
        self.c_pixel = c_pixel
        self.num_block = num_block
        
        self.r_block = self.r_pixel / self.num_block
        self.c_block = self.c_pixel / self.num_block
        
                        
    def generate_pixels1(self):
        self.pixels = NP.zeros((self.c_pixel, self.r_pixel), dtype='bool')
        #all black to begin with        
        for j in NP.arange(self.num_block):
            for i in NP.arange(self.num_block):
                if (j + i ) % 2 == 1:
                    self.pixels[j*self.c_block:(j+1)*self.c_block:1, i*self.r_block:(i+1)*self.r_block:1] = 1
                    
    def generate_pixels2(self):
        a = NP.fromfunction(lambda i, j: i % self.c_block * 2 < self.c_block, (self.c_pixel, self.r_pixel), dtype=int)
        b = NP.fromfunction(lambda i, j: j % self.r_block * 2 < self.r_block, (self.c_pixel, self.r_pixel), dtype=int)        
        self.pixels = a-b
                    
    def generate_pixels3(self):
        black_block = NP.zeros((self.c_block, self.r_block))
        white_block = NP.ones((self.c_block, self.r_block))
        two_block1 = NP.hstack((black_block, white_block))
        two_block2 = NP.hstack((white_block, black_block))        
        four_block = NP.vstack((two_block1, two_block2))
        self.pixels = NP.tile(four_block, (self.num_block/2, self.num_block/2))
        
    def generate_pixels4(self):
        c = NP.arange(0, self.c_pixel, 1)
        r = NP.arange(0, self.r_pixel, 1)
        C, R = meshgrid(c, r)        
        self.pixels = NP.remainder(C % 200 < 100)
        self.pixels = NP.remainder(R % 200 < 100)
                                         
    def render(self):
        MPL.imshow(self.pixels, cmap = cm.gist_gray)
        MPL.show()
        
  
cb = CheckerBoard()
cb.generate_pixels3()
cb.render()