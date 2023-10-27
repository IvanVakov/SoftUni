annual_tax_train = int(input())

basketball_sneakers = annual_tax_train - (annual_tax_train * 0.4)
basketball_jersey = basketball_sneakers - (basketball_sneakers * 0.2)
basketball_ball = basketball_jersey / 4
basketball_acc = basketball_ball / 5

total_cost = annual_tax_train + basketball_sneakers + basketball_jersey + basketball_ball + basketball_acc

print(total_cost)