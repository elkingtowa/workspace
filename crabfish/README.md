Crabfish
--------

Crabfish is a chess engine in Python

Screenshot
--------

    My move: g8f6
                      
                       
       r n b q k b . r 
       p p p p p p p p 
       . . . . . n . . 
       . . . . . . . . 
       . . . . P . . . 
       . . . . . . . . 
       P P P P . P P P 
       R N B Q K B N R 
                       
                        
    Your move: 


Run it
--------

On Mac:
python crabfish.py in the terminal


Features
--------

1. Build around the simple, but deadly efficient MTD-bi search algorithm.
2. Filled with classic as well as modern 'chess engine tricks' for simpler and faster code.
3. Easily adaptive evaluation function through Piece Square Tables.
4. Uses standard Python collections and data structures for clarity and efficiency.

Things to add
--------

minor promotion 
draws of any kind
Expand input beyond two coordinate notation
piecelist to save the enumeration of all board squares at every move generation
dedicated check detection
zobrist hashing
mutable board representation (i.e. bitboard)
distinguish between midgame and endgame
threat detection
advanced move ordering (i.e. killer move and SEE)