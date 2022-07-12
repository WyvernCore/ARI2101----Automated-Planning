(define (problem problem2)
	(:domain slidingtilepuzzle)
	
	(:objects
	l1 - location
	l2 - location
	l3 - location
	l4 - location
	l5 - location
	l6 - location
	l7 - location
	l8 - location
	l9 - location
	t1 - tile
	t2 - tile
	t3 - tile
	t4 - tile
	t5 - tile
	t6 - tile
	t7 - tile
	t8 - tile
	)
	
	(:init
    (leftof l1 l2)
    (topof l1 l4)
    (leftof l2 l3)
    (topof l2 l5)
    (rightof l2 l1)
    (topof l3 l6)
    (rightof l3 l2)
    (bottomof l4 l1)
    (leftof l4 l5)
    (topof l4 l7)
    (bottomof l5 l2)
    (leftof l5 l6)
    (topof l5 l8)
    (rightof l5 l4)
    (bottomof l6 l3)
    (topof l6 l9)
    (rightof l6 l5)
    (bottomof l7 l4)
    (leftof l7 l8)
    (bottomof l8 l5)
    (leftof l8 l9)
    (rightof l8 l7)
    (bottomof l9 l6)
    (rightof l9 l8)
    (at t1 l1)
    (at t2 l2)
    (at t3 l3)
    (at t4 l4)
    (at t6 l5)
    (empty l6)
    (at t7 l7)
    (at t5 l8)
    (at t8 l9)
    )
    
	(:goal (and
	(at t1 l1)
    (at t2 l2)
    (at t3 l3)
    (at t4 l4)
    (at t5 l5)
    (at t6 l6)
    (at t7 l7)
    (at t8 l8)
    (empty l9)
	))
)