# nums = [1, 3, 5, 2, 4, 3, 3, 3]
# print (len(nums))
# #itvlis siashi myof elementebs
# surname = "keshelava"
# print(len(surname))
# set_of_nums = set(nums)
# print(set_of_nums)

# letters = ["a", "b", "c"]

# letters += ["d", "e"]

# print(len(letters))
# print(letters)


# words = ["Python", "fun"]
# words.insert(1, "is") #სასურველი ელემენტის ჩასმა მითითებულ პოზიციაზე
# #       სად ჩაჯდეს, რა ჩაჯდეს
# print(words)


# შექმენით სია დედიკოსგან და მამიკოსგან,

# შუაში ჩასვით თქვენი თავი,
# ხოლო ბოლოში ჩასვით კიდევ ერთი საყვარელი ადამიანი

# famyly = ["mum","dad"]

# famyly.append("robi")

# famyly.insert(1,"me")

# nums = [4, 5, 6]
# msg = "Numbers: {0} {1} {2}". format(nums[2], nums[3], nums[1])
# print(msg)


#შექმენით თქვენი ოჯახის წევრებისგან სია

# და ჩააფორმატეთ მათი სახელები ამ წინადადებაში:

# "ჩემი დედიკოა ----, ჩემი მამიკოა ----, მე ვარ  ----"



# nums = [1, 3, 5, 2, 4, 3, 3, 3]
# # print (len(nums))
# #   #itvlis siashi myof elementebs

# # surname = "keshelava"
# # print(len(surname))

# set_of_nums = set(nums)
# print(set_of_nums)


# letters = ["a", "b", "c"]

# letters += ["d", "e"]

# print(len(letters))
# print(letters)

# nums = [1, 2, 3]
# nums.append(20) #amatebs elements siis boloshi
# print(nums)

# words = ["Python", "fun"]
#           #0      
# words.insert(1, "is") #amatebs sasurvel elements siis sasurvel poziciaze
#      #სად ჩაჯდეს #რა ჩაჯდეს
# print(words)


# family = ["dzamiko", "mom", "dad"]
# family.insert(2, "mate")
# family.append("saba")
# print(family)


# nums = [9, 8, 7, 6, 5] #შეიქმნა სია 5 ელემენტისგან

# nums.append(4) #ჩაისვა ელემენტი სიის ბოლოში ამ შემთხვევაში 4
#                #[9, 8, 7, 6, 5, 4]
# nums.insert(2, 11) #7ის წინ ჩაისვა 11 მეორე პოზიციაზე
#          #[9, 8, 11, 7, 6, 5, 4]
# print(len(nums)) #დაითვალა ელემენტები სიაში და გამოიტანა ტერმინალში

#lenს აქვს სხვადასხვა გამოყენება 
#1- ის ითვლის სიაში ელემენტების რაოდენობას
#2- ის ითვლის stringში სიმბოლოეების რაოდენობას

# letters = ['p', 'q', 'r', 's', 'p', 'u']
# print(letters.index('r'))
# print(letters.index('p'))
# print(letters.index('q'))

# x = [1, 8, 42, 3]

# print(min(x)) #მინიმალური რიცხვი სიიდან (ყველაზე პატარა)
# print(max(x)) #მაქსიმალური რიცხი სიიდან (ყველაზე დიდი)


# nums = [1, 3, 5, 2, 4]

# res = min(nums) + max(nums)

# print(res)


# x = [2, 4, 6, 2, 4, 7, 2, 9]
# print(x.count(2))#ითვლის სიაში რამდენჯერ არის ელემენტი მოცემული

# x.remove(4) #შლის სიიდან კონკრეტულ ელემენტს
# print(x)

# x.reverse() #აბრუნებს სიას უკუღმა
# print(x)

# age = int(input("sheiyvanet asaki: "))
# if age >18 :
#   print("srulwlovani xar")
# else:
#   print("bavshvi xar kiddo")



# nums = [2,4,8,9,5]


# nums.insert(1, 3) #[2,3,4,8,9,5]

# nums.remove(9) #[2,3,4,8,5]

# nums.insert(0, nums.count(8)) #[1,2,3,4,8,5]

# print(nums[3]) #4 


# nums = [4, 5, 6]
# msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
# print(msg)


# family = ["tamuna", "saba", "mate"]
# fam = "My mother is: {}".format(family[0])
# print(fam)
# fam = "My brother is: {}".format(family[1])
# print(fam)
# fam = "My name is: {}".format(family[2])
# print(fam)

# a = "my name is: {}".format("nika")
# print(a)

# a = "my name is: {} my surname is: {}".format("keshelava", "nika")
# print(a)

# family = ["tamuna", "saba", "mate"]
# full_sentence = "My moms name is: {}, My brothers name is: {}, My name is: {}".format(family[0],family[1],family[2])
# print(full_sentence)

