# -*- coding: utf-8 -*-

__author__ = "Nico David Moric, Johannes Lepakorpi"
__copyright__ = "No Copyright Yet"
__credits__ = "Nico David Moric, Johannes Lepakorpi"
__license__ = "MIT"
__version__ = "0.0.0.0.1"
__maintainer__ = "Nico David Moric, Johannes Lepakorpi"
__email__ = "thekoolaidmannn@gmail.com , ," # Include Johanne's Email
__status__ = "Production"
__name__ = "AZORIAN"
__dates__ = "October 2 - October 14"
__company__ = "Bio-Logyk"

import sys
import wikipedia
import time

Options_List = ["Sequence Input", "Animal Info", "Add New Document"]  # Add more things to this list

class Animal: # This class is for the choice of animal
    def __init__(self, animal):
        self.animal = animal

dna_codon_to_amino_acid = {"TTT" : "Phe", "TTC" : "Phe", "TTA" : "Leu", "TTG" : "Leu", "TCT" : "Ser", "TCC" : "Ser",
                        "TCA" : "Ser", "TCG" : "Ser", "TAT" : "Tyr", "TAC" : "Tyr", "TAA" : "STOP", "TAG" : "STOP",
                        "TGT" : "Cys", "TGC" : "Cys", "TGA" : "STOP", "TGG" : "Trp", "CTT" : "Leu", "CTC" : "Leu",
                        "CTA" : "Leu", "CTG" : "Leu", "CCT" : "Pro", "CCC" : "Pro", "CCA" : "Pro", "CCG" : "Pro",
                        "CAT" : "His", "CAC" : "His", "CAA" : "Gln", "CAG" : "Gln", "CGT" : "Arg", "CGC" : "Arg",
                        "CGA" : "Arg", "CGG" : "Arg", "ATT" : "Ile", "ATC" : "Ile", "ATA" : "Ile", "ATG" : "Met",
                        "ACT" : "Thr", "ACC" : "Thr", "ACA" : "Thr", "ACG" : "Thr", "AAT" : "Asn","AAC" : "Asn",
                        "AAA" : "Lys", "AAG" : "Lys", "AGT" : "Ser", "AGC" : "Ser", "AGA" : "Arg", "AGG" : "Arg",
                        "GTT" : "Val", "GTC" : "Val", "GTA" : "Val", "GTG" : "Val", "GCT" : "Ala", "GCC" : "Ala",
                        "GCA" : "Ala", "GCA" : "Ala", "GCG" : "Ala", "GAT" : "Asp", "GAC" : "Asp", "GAA" : "Glu",
                        "GAG" : "Glu", "GGT" : "Gly", "GGC" : "Gly", "GGA" : "Gly", "GGG" : "Gly"}

rna_codon_to_amino_acid = {"UUU" : "Phe", "UUC" : "Phe", "UUA" : "Leu", "UUG" : "Leu", "UCU" : "Ser", "UCC" : "Ser",
                        "UCA" : "Ser", "UCG" : "Ser", "UAU" : "Tyr", "UAC" : "Tyr", "UAA" : "STOP", "UAG" : "STOP",
                        "UGU" : "Cys", "UGC" : "Cys", "UGA" : "STOP", "UGG" : "Trp", "CUU" : "Leu", "CUC" : "Leu",
                        "CUA" : "Leu", "CUG" : "Leu", "CCU" : "Pro", "CCC" : "Pro", "CCA" : "Pro", "CCG" : "Pro",
                        "CAU" : "His", "CAC" : "His", "CAA" : "Gln", "CAG" : "Gln", "CGU" : "Arg", "CGC" : "Arg",
                        "CGA" : "Arg", "CGG" : "Arg", "AUU" : "Ile", "AUC" : "Ile", "AUA" : "Ile", "AUG" : "Met",
                        "ACU" : "Thr", "ACC" : "Thr", "ACA" : "Thr", "ACG" : "Thr", "AAU" : "Asn", "AAC" : "Asn",
                        "AAA" : "Lys", "AAG" : "Lys", "AGU" : "Ser", "AGC" : "Ser", "AGA" : "Arg", "AGG" : "Arg",
                        "GUU" : "Val", "GUC" : "Val", "GUA" : "Val", "GUG" : "Val", "GCU" : "Ala", "GCC" : "Ala",
                        "GCA" : "Ala", "GCA" : "Ala", "GCG" : "Ala", "GAU" : "Asp", "GAC" : "Asp", "GAA" : "Glu",
                        "GAG" : "Glu", "GGU" : "Gly", "GGC" : "Gly", "GGA" : "Gly", "GGG" : "Gly"}

#time.sleep(3)
print("\n\nWelcome")
print("\n\nThis is the Azorian Project")
print("\n\nMade by BIO-LOGYK©")
#time.sleep(3)

def new():
    print("\n\nSelect below which options you want\n\n")
    print(', '.join(Options_List))

    choice = input()

    if (choice.lower() == "sequence input"):
        print("\n\nGoing to Sequence Input")
        #time.sleep(3)

        while True:
            print("\n\nEnter a sequence to begin: (blank to quit)")
            sequenceI = input()
            if sequenceI == "":
                break

            check_point = 0
            to_point = 3

            for i in range(int(len(sequenceI) / 3)):
                if sequenceI[check_point:to_point] in dna_codon_to_amino_acid:
                    print(dna_codon_to_amino_acid[
                              sequenceI[check_point:to_point]] + " gives the Codon value of " + sequenceI[check_point:to_point])
                check_point += 3
                to_point += 3

            while True:
                print("\n\nEnter a sequence to begin: (blank to quit)")
                sequenceII = input()
                if sequenceII == "":
                    break

                check_point = 0
                to_point = 3

                for i in range(int(len(sequenceII) / 3)):
                    if sequenceII[check_point:to_point] in rna_codon_to_amino_acid:
                        print(rna_codon_to_amino_acid[
                                  sequenceII[check_point:to_point]] + " gives the Codon value of " + sequenceII[check_point:to_point])
                    check_point += 3
                    to_point += 3

            # else:
            # print("I do not have enough information " +sequenceI)
            # print("\n\nWhat is the sequence again")
            # sequenceII = input()
            # dna_codon_to_amino_acid[sequenceI] = sequenceII
            # print("\n\nUpdated")

    elif (choice == "Animal Info"):
        print("\n\nGoing to Animal Info")
        time.sleep(3)
        print("Enter an animal you want more info on")
        animal = input()
        print(wikipedia.summary(animal))

    elif (choice == "Add New Document"):
        print("\n\nSetting up Document")
        time.sleep(3)

    else:
        print("\n\nLooks like you selected none of the inputs that are available try again")
        time.sleep(3)
        new()

print("\n\nSelect below which options you want\n\n")
print(', '.join(Options_List))

choice = input()

if (choice.lower() == "sequence input"):
    print("\n\nGoing to Sequence Input")
    # time.sleep(3)

    while True:
        print("\n\nEnter a sequence to begin: (blank to quit)")
        sequenceI = input()
        if sequenceI == "":
            break

        check_point = 0
        to_point = 3

        for i in range(int(len(sequenceI) / 3)):
            if sequenceI[check_point:to_point] in dna_codon_to_amino_acid:
                print(dna_codon_to_amino_acid[
                          sequenceI[check_point:to_point]] + " gives the Codon value of " + sequenceI[
                                                                                            check_point:to_point])
            check_point += 3
            to_point += 3

        while True:
            print("\n\nEnter a sequence to begin: (blank to quit)")
            sequenceII = input()
            if sequenceII == "":
                break

            check_point = 0
            to_point = 3

            for i in range(int(len(sequenceII) / 3)):
                if sequenceII[check_point:to_point] in rna_codon_to_amino_acid:
                    print(rna_codon_to_amino_acid[
                              sequenceII[check_point:to_point]] + " gives the Codon value of " + sequenceII[
                                                                                                 check_point:to_point])
                check_point += 3
                to_point += 3

        # else:
        # print("I do not have enough information " +sequenceI)
        # print("\n\nWhat is the sequence again")
        # sequenceII = input()
        # dna_codon_to_amino_acid[sequenceI] = sequenceII
        # print("\n\nUpdated")

elif (choice == "Animal Info"):
    print("\n\nGoing to Animal Info")
    time.sleep(3)
    print("Enter an animal you want more info on")
    animal = input()
    print(wikipedia.summary(animal))

elif (choice == "Add New Document"):
    print("\n\nSetting up Document")
    time.sleep(3)

else:
    print("\n\nLooks like you selected none of the inputs that are available try again")
    time.sleep(3)
    new()
