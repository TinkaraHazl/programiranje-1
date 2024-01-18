(* 1. a) *)
let zamenjaj (a, b) (c, d) = (a, c) (b, d)

(* 1. b) *)
let modus a b c =
  if a = b then Some a
  else if a = c then Some a
  else if b = c then Some b
  else None

(* 1. c) *)
let uncons list = match list with
|[] -> None
|x :: xs -> Some(x, xs)

(* 1. d) *)
let vstavljaj a list =
  let rec vstavljaj_aux a list acc = match list with
  |[] -> List.rev acc
  |x :: xs -> vstavljaj_aux a xs (a :: x :: acc)
in vstavljaj_aux a list []

(* 1. e) *)
let popolnoma_obrni list =
  let rec popolnoma_obrni_aux list acc1 = match list with
  |[] -> acc1
  |x :: xs -> 
    let obrni list acc2 = match list with
    |[] -> acc2
    |x :: xs -> obrni list (x :: acc2)
    in obrni list []
  in popolnoma_obrni_aux xs ((obrni xs) :: acc1)

