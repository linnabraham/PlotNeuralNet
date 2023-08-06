
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input('galaxy.jpg'),
    to_Conv("conv0", 224, 3, offset="(0,0,0)", to="(0,0,0)", height=42, depth=42, width=3 ),
    to_Conv("conv1", 5, 96, offset="(1,0,0)", to="(conv0-east)", height=10, depth=10, width=5 ),

    to_connection("conv0", "conv1"),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", height=5, depth=5, width=1),
    to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=5, depth=5, width=10 ),
    to_connection( "pool1", "conv2"),


    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=3, depth=3, width=1),

    to_Conv("conv3", 128, 64, offset="(1,0,0)", to="(pool2-east)", height=3, depth=3, width=15 ),

    to_connection("pool2", "conv3"),

    to_Conv("conv4", 128, 64, offset="(1,0,0)", to="(conv3-east)", height=3, depth=3, width=15 ),

    # to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    # to_connection("pool2", "soft1"),
    # to_Sum("sum1", offset="(1.5,0,0)", to="(soft1-east)", radius=2.5, opacity=0.6),
    # to_connection("soft1", "sum1"),
    to_connection("conv3", "conv4"),

    to_Conv("conv5", 512, 64, offset="(1,0,0)", to="(conv4-east)", height=3, depth=3, width=13 ),

    to_connection("conv4", "conv5"),

    to_Pool("pool3", offset="(0,0,0)", to="(conv5-east)", height=2, depth=2, width=1),
    to_Conv("fc1", 4096, 1, offset="(1,0,0)", to="(conv5-east)", height=1, depth=30, width=1 ),

    to_connection("pool3", "fc1"),
    to_Conv("fc2", 4096, 1, offset="(1,0,0)", to="(fc1-east)", height=1, depth=30, width=1 ),

    to_connection("fc1", "fc2"),
    to_Conv("fc3", 1000, 1, offset="(1,0,0)", to="(fc2-east)", height=2, depth=20, width=1 ),

    to_connection("fc2", "fc3"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
