import actions as a
import random as r
import warrior as w
import text

def start():
    warrior1 = w.Warrior('Leonidas I of Sparta')
    warrior2 = w.Warrior('Richard The Lionheart')

    while True:


        fighters = [warrior1, warrior2]

        res = {
            warrior1._name:0,
            warrior2._name:0
        }

        attempts = 5
        a.print_message(text.message_start)
        a.print_message(text.warrior1)
        a.print_message(warrior1)

        a.print_message(text.warrior2)
        a.print_message(warrior2)
        while attempts > 0:

            a.print_message(text.message_strike)

            for person in fighters:
                enemy_strike = r.randint(1, 10)
                a.print_message(person, f'He got strike {enemy_strike}')
                person.attack(enemy_strike)

            winner = max(fighters)
            res[winner._name]+=1

            a.print_message(text.message_end_round)
            attempts-=1
            if not all(list(map( lambda x: x.alive(), fighters))):
                break

        winner = max(res.items(), key=lambda x: x[1])[0]
        for wr in fighters:
            if wr._name==winner:
                wr._power+=1

        a.print_message(text.message_end)
        a.print_message(f'{">"*40}',winner.upper(),f'{"<"*40}')



        if not all(list(map( lambda x: x.alive(), fighters))):
            a.print_message(text.death_message)
            break
        a.print_message(text.end_game)
        if input()=='N':
            break

