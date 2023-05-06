class Ship:
    def __init__(self, draft, crew):
        Ship.draft = draft
        Ship.crew = crew
         
    def is_worth_it(self):
        return self.draft-(self.crew * 1.5) > 20


Titanik = Ship(50, 0)
print(Titanik.is_worth_it())    

# class External_Ship(Ship):
#     def __init__(self, draft, crew):
#         Ship.draft = int(draft) + 50
#         Ship.crew = int(crew) + 10

# Titanik = External_Ship(50, 0)
# print(Titanik.draft)

