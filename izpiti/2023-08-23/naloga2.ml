type player = White | Black

type game_tree =
  | Winner of player
  | Tie
  | Decision of player * (float * game_tree) list

let primer =
  Decision
    ( White,
      [
        (0.3, Decision (Black, [ (0.5, Winner White); (0.5, Winner Black) ]));
        (0.7, Decision (Black, [ (0.5, Tie); (0.5, Winner Black) ]));
      ] )

(* 1. a) *)
let prestej_zmage game_tree = 
  let rec stej_bele game_tree acc = match game_tree with
  |Decision (player1, [(p1, tree1), (p2, tree2)]) -> stej_bele tree acc
  |Tie -> 
  |Winner (player) -> match player with
                    |White -> acc + 1
                    |Black -> acc
  in stej_bele game_tree 0

(* 1. b) *)
type result = { white_wins : float; black_wins : float; ties : float }

(* 1. c) *)

(* 1. d) *)
