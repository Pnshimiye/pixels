from django.apps import AppConfig


class MygalleryConfig(AppConfig):
    name = 'myGallery'


def dashatize(num):
  
    b = str(num)
    nums = []
    index=0
    for digit in b:
        nums.append(int(digit))
    for n in nums:
        if n%2!=0:


            nums.insert((nums.index(n)),"-")
            nums.insert((nums.index(n)+1),"-")
    return nums 

