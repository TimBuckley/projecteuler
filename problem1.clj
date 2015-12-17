(apply + 
       (filter
        (fn [n]
          (or (zero? (mod n 5)) (zero? (mod n 3))))
        (range 1000)))
;=> 233168
