# ბილეთი ღირს 25 ლარი,
# მაგრამ ბავშვებისთვის უფასოა,
# გვყავს 13 ადამიანი, აქედან 10 დიდი და 3 ბავშვი, 
# გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ 
ticket_cost = 25
num_adults = 10
total_cost = 0
person_count = 0
while person_count < 13:
    if person_count < num_adults:
        total_cost += ticket_cost
    else:
        break
    person_count += 1

    if person_count % 3 == 0:
        continue
print(total_cost)