#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:12:13 2018

@author: kinchunglam
"""
import random
class sic_bo:
    def __init__(self):
        self.dice1 = 0
        self.dice2 = 0
        self.dice3 = 0
        self.result = []

    def roll_dices(self):
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        self.dice3 = random.randint(1,6)
        return [self.dice1,self.dice2,self.dice3]
    
    def multi_roll_dices(self,times):
        for i in range(times):
            self.result.append(self.roll_dices())
        return self.result
class judge:
    def big_or_small(game_result):
        result = []
        for i in game_result:
            if sum(i) >=11:
                result.append("b")
            else:
                result.append("s")
        return result
            
class gambler:
    def __init__(self,money,game):
        self.money = money
        self.game = game
        