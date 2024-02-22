type 'a tape = Tape of { left : 'a list; head : 'a; right : 'a list }

type 'a command = Left | Do of ('a -> 'a) | Right

let example = Tape { left = [ 3; 2; 1 ]; head = 4; right = [ 5; 6 ] }

(* 2. a) *)

let map tape f = match tape with
|Tape {left = l; head = h; right = r} -> Tape {left = (List.map f l); head = (f h); right = (List.map f r)}

(* 2. b) *)

let izvedi tape cmd = match cmd with
|Right -> (match tape with
  |Tape {left = l; head = h; right = []} -> None
  |Tape {left = l; head = h; right = x :: xs} -> Some (Tape {left = (l @ [h]); head = x; right = xs}))
|Left -> None (* match tape with
  |Tape {left = []; head = h; right = r} -> None
  |Tape {left = (xs @ [x]); head = h; right = r} -> Some (Tape {left = xs ; head = x; right = (h :: r)})*)
|Do f -> None (*match tape with 
  | Tape {left = h; head = h; right = r} -> Some (Tape {left = l; head = (f h); right = r})*)


(* 2. c) *)

let izvedi_ukaze _ = failwith "TODO"

(* 2. d) *)

let naberi_in_pretvori _ = failwith "TODO"

(* 2. e) *)

let pripravi_ukaze _ = failwith "TODO"
