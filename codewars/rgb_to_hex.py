#  File name: rgb_to_hex.py
#  Developed by Yuriy Kondrashov on 2/2/20 7:47 PM
#  Date last modified: 2/2/20 7:46 PM
#  Copyright (c) 2020. All rights reserved.


def rgb_to_hax(r, g, b):
    return ''.join(['%02X' % max(0, min(x, 255)) for x in [r, g, b]])


# def rgb_to_hax(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))


# num_tab = tuple(range(16))
# hax_tab = tuple(num_tab[:10] + ("A", "B", "C", "D", "E", "F"))
#
#
# def rgb_to_hax(r, g, b):
#     hax = []
#     for x in (r, g, b):
#         x = 0 if x < 0 else x
#         x = 255 if x > 255 else x
#         x1 = x // 16
#         x2 = int(((x / 16) - x1) * 16)
#         hax.append(str(hax_tab[x1]))
#         hax.append(str(hax_tab[x2]))
#     return ''.join(hax)



    # rgb = []
    # for x in (r, g, b):
    #     x = 0 if x < 0 else x
    #     x = 255 if x > 255 else x
    #     rgb.append(x)
    # r, g, b = rgb
    # rgb = zip([x//16 for x in (r,g,b)],[int(((y/16)-(y//16))*16) for y in (r,g,b)])
    # for x, y in rgb:
    #     if x in range(10):
    #
    #     print(x,y)



if __name__ == '__main__':
    print(rgb_to_hax(0,0,0)) # "000000", "testing zero values"
    print(rgb_to_hax(1,2,3)) # "010203", "testing near zero values"
    print(rgb_to_hax(255,255,255)) # "FFFFFF", "testing max values"
    print(rgb_to_hax(254,253,252)) # "FEFDFC", "testing near max values"
    print(rgb_to_hax(-20,275,125)) # "00FF7D", "testing out of range values"
