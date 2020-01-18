import math

import numpy

# triangle_area_1 = 0
# triangle_area_2 = 0
# l1 = 3.5
# l2 = 1
# l3 = 3
# l4 = 2
#
# minimum_length = abs(l1 - l2)
# maximum_length = l1 + l2
# print('minimum:  ', minimum_length, 'maximum:  ', maximum_length)
# for diagonal_length in numpy.arange(minimum_length, maximum_length, 0.1):
#     semi_perimeter = (l1 + l2 + diagonal_length) / 2
#     temp_triangle_area = (
#         math.sqrt(
#             semi_perimeter *
#             (semi_perimeter - l1) *
#             (semi_perimeter - l2) *
#             (semi_perimeter - diagonal_length))
#     )
#     if temp_triangle_area < triangle_area_1:
#         diagonal_length = diagonal_length - 0.1
#         print('diagonal: ', diagonal_length)
#         semi_perimeter = (l3 + l4 + diagonal_length) / 2
#         triangle_area_2 = (
#             math.sqrt(
#                 semi_perimeter *
#                 (semi_perimeter - l3) *
#                 (semi_perimeter - l4) *
#                 (semi_perimeter - diagonal_length))
#         )
#         break
#     triangle_area_1 = temp_triangle_area
#
# quadrilateral_area = triangle_area_1 + triangle_area_2
# print('triangle area 1  :    ', triangle_area_1, 'triangle area 2:  ', triangle_area_2)
# print('area:    ', quadrilateral_area)


triangle_area_1 = 0
triangle_area_2 = 0
l1 = 6.3
l2 = 15.2
l3 = 10.2
l4 = 13.2

minimum_length = abs(l1 - l2)
maximum_length = l1 + l2
print('minimum:  ', minimum_length, '/n', 'maximum:  ', maximum_length)
for diagonal_length in numpy.arange(minimum_length, maximum_length, 0.001):
    semi_perimeter = (l1 + l2 + diagonal_length) / 2
    temp_triangle_area = (
        math.sqrt(
            semi_perimeter *
            (semi_perimeter - l1) *
            (semi_perimeter - l2) *
            (semi_perimeter - diagonal_length))
    )
    if temp_triangle_area < triangle_area_1:
        diagonal_length = diagonal_length - 0.1
        print('diagonal: ', diagonal_length)
        semi_perimeter = (l3 + l4 + diagonal_length) / 2
        triangle_area_2 = (
            math.sqrt(
                semi_perimeter *
                (semi_perimeter - l3) *
                (semi_perimeter - l4) *
                (semi_perimeter - diagonal_length))
        )
        break
    triangle_area_1 = temp_triangle_area

quadrilateral_area = triangle_area_1 + triangle_area_2
print('triangle area 1  :    ', triangle_area_1, 'triangle area 2:  ', triangle_area_2)
print('area:    ', quadrilateral_area)

# feet = 5.5
# l1 = 32 * feet
# l1p1 = l1
# l1p2 = l1
#
# l2 = 55 * feet
# l2p1 = l2
# l2p2 = l2
#
# l3 = 7 * feet
# l3p1 = l3
# l3p2 = l3
#
# l4 = 67 * feet
# l4p1 = l4
# l4p2 = l4
# #
# # l1p1 = l1p1 - 1
# print(12 / 10)
# print(1.2 * 5)
# print(7 / 1.2)
# for length 1 point 1
# h = 40.5
# l1 = 22
# l2 = 31
# l3 = 15
# l4 = 41


# h = 3.6
# l1 = 3.5
# l2 = 1
# l3 = 3
# l4 = 2

# l1 = 52
# l2 = 39
# l3 = 25
# l4 = 60
# min = abs(l1 - l2)
# max = l1 + l2

# print("max: ", max)
# print("min: ", min)
# area1 = 0
# area2 = 0
# # temp = 0
# for h in numpy.arange(min, max, 0.1):
#
#     s = (l3 + l4 + h) / 2
#     heron2 = math.sqrt(s * (s - l3) * (s - l4) * (s - h))
#     # print('s', s)
#     # s2 = (l3 + l4 + h) / 2
#     # print(s2)
#     # heron2 = math.sqrt(s2 * (s2 - l3) * (s2 - l4) * (s2 - h))
#     # temp = heron1 + heron2
#
#     if heron2 < area2:
#         h = h - 0.1
#         print(h)
#         print('area2:    ', area2)
#         s = (l1 + l2 + h) / 2
#         heron1 = math.sqrt(s * (s - l1) * (s - l2) * (s - h))
#         area1 = heron1
#         print('area1:    ', area1)
#         print('whole area: ', area1 + area2)
#         print('marlay          ', (area1 + area2) / 272.25)
#         break
#     area2 = heron2

# area2 = 0
# temp = 0
# for h in numpy.arange(min, max, 0.1):
#     print(h)
#
#     s = (l3 + l4 + h) / 2
#     heron2 = math.sqrt(s * (s - l3) * (s - l4) * (s - h))
#     # print('s', s)
#     # s2 = (l3 + l4 + h) / 2
#     # print(s2)
#     # heron2 = math.sqrt(s2 * (s2 - l3) * (s2 - l4) * (s2 - h))
#     # temp = heron1 + heron2
#
#     if heron2 < area2:
#         break
#     area2 = heron2
#
# print('area2:    ', area2)
# print('whole area: ', area1 + area2)
# if l1p1 < l1:
#     temp = l1 - l1p1
#     l2p1 = l2p1 + temp
#     l1 = l1p1
#
# elif l1p1 > l1:
#     temp = l1p1 - l1
#     l2p1 = l2p1 + temp
#     l1 = l1p1
#
# # for length 1 point 2
#
# if l1p2 < l1:
#     temp = l1 - l1p2
#     l4p1 = l4p1 + temp
#     l1 = l1p2
#
# elif l1p2 > l1:
#     temp = l1p2 - l1
#     l4p1 = l4p1 + temp
#     l1 = l1p1
#
# # for length 2 point 1
#
# if l2p1 < l2:
#     temp = l2 - l2p1
#     l1p1 = l1p1 + temp
#     l2 = l2p1
#
# elif l2p1 > l2:
#     temp = l2p1 - l2
#     l1p1 = l1p1 + temp
#     l2 = l2p1
#
# # for length 2 point 2
#
# if l2p2 < l2:
#     temp = l2 - l2p2
#     l3p1 = l3p1 + temp
#     l2 = l2p2
#
# elif l2p2 > l2:
#     temp = l2p2 - l2
#     l3p1 = l3p1 + temp
#     l2 = l2p2
#
# # for length 3 point 1
#
# if l3p1 < l3:
#     temp = l3 - l3p1
#     l2p2 = l2p2 + temp
#     l3 = l3p1
#
# elif l3p1 > l3:
#     temp = l3p1 - l3
#     l2p2 = l2p2 + temp
#     l3 = l3p1
#
# # for length 3 point 2
#
# if l3p2 < l3:
#     temp = l3 - l3p2
#     l4p2 = l4p2 + temp
#     l3 = l3p2
#
# elif l3p2 > l3:
#     temp = l3p2 - l3
#     l4p2 = l4p2 + temp
#     l3 = l3p2
#
# # for length 4 point 1
#
# if l4p1 < l4:
#     temp = l4 - l4p1
#     l1p1 = l1p1 + temp
#     l4 = l4p1
#
# elif l4p1 > l4:
#     temp = l4p1 - l4
#     l1p1 = l1p1 + temp
#     l4 = l4p1
#
# # for length 4 point 2
#
# if l4p2 < l4:
#     temp = l4 - l4p2
#     l3p2 = l3p2 + temp
#     l4 = l4p2
#
# elif l4p2 > l4:
#     temp = l4p2 - l4
#     l3p2 = l3p2 + temp
#     l4 = l4p2
#
# print(l1, '     ', l2, ' ', l3, ' ', l4)

l1 = 6.3
l2 = 15.2
l3 = 10.2
l4 = 13.2
s = (l1 + l2 + 17) / 2
heron = math.sqrt(s * (s - l1) * (s - l2) * (s - 17))
s = (l3 + l4 + 17) / 2
heron1 = math.sqrt(s * (s - l3) * (s - l4) * (s - 17))

print('aa', heron + heron1)
