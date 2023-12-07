open System.IO
open System.Text.RegularExpressions
open System
open System.Linq

let readLines (filePath: string) =
    seq {
        use sr = new StreamReader(filePath)

        while not sr.EndOfStream do
            yield sr.ReadLine()
    }

let rec getLists (lines: list<string>) (bid: list<list<char>>) (values: list<int>) =
    match lines with
    | [] -> (bid, values)
    | h :: t ->
        let splited = h.Split(" ")
        let arr = splited[0].ToCharArray() |> Array.toList
        getLists t (arr :: bid) (int (splited[1]) :: values)

let matchesToIntList (matchCollection: MatchCollection) =
    matchCollection
    |> Seq.cast<System.Text.RegularExpressions.Match>
    |> Seq.toList
    |> List.map (fun m -> int64 (m.Value))

let rec createDict (bid: list<list<char>>) (values: list<int>) (maps: list<Map<char, int> * int * list<char>>) =
    match (bid, values) with
    | [], [] -> maps |> List.rev
    | h :: t, hv :: tv ->
        let x = h |> List.countBy id |> Map.ofList
        createDict t tv ((x, hv, h) :: maps)



let matchNumbers (line: string) = Regex.Matches(line, @"(\d+)")
let dayInput = readLines ("./day-7.txt") |> Seq.toList
let (bid, values) = getLists dayInput [] []
let z = createDict bid values []

let rec sumList (maps: list<Map<char, int> * int * list<char>>) (sum: int) (idx: int) =
    match maps with
    | [] -> sum
    | (c, v, s) :: t -> sumList t ((idx * v) + sum) (idx + 1)

let cardsDay2 =
    [| 'A'; 'K'; 'Q'; 'T'; '9'; '8'; '7'; '6'; '5'; '4'; '3'; '2'; 'J' |]
    |> Array.rev

let cards =
    [| 'A'; 'K'; 'Q'; 'J'; 'T'; '9'; '8'; '7'; '6'; '5'; '4'; '3'; '2' |]
    |> Array.rev


let sorted =
    z
    |> List.sortBy (fun (cardMap, value, hand) ->
        let sortByType = cardMap |> Map.toSeq |> Seq.map snd |> Seq.max

        let countOfMax =
            cardMap
            |> Map.toSeq
            |> Seq.map snd
            |> Seq.filter (fun el -> el = sortByType)
            |> Seq.length

        let checkIfFullHouseOrTwoPairs =
            if
                ((sortByType = 3 && cardMap.Values.Contains(2))
                 || (sortByType = 2 && countOfMax = 2))
            then
                1
            else
                0


        let sortByFigure =
            hand
            |> List.toArray
            |> Array.map (fun c -> cards |> Array.findIndex (fun q -> q = c))

        (sortByType, checkIfFullHouseOrTwoPairs, sortByFigure))


let sortedDay2 =
    z
    |> List.sortBy (fun (cardMap, value, hand) ->
        let maxCardCount = cardMap |> Map.toSeq |> Seq.map snd |> Seq.max
        let joker = cardMap.TryFind 'J'

        let jokersCount =
            match joker with
            | Some o -> o
            | None -> 0


        let countOfMax =
            cardMap
            |> Map.toSeq
            |> Seq.map snd
            |> Seq.filter (fun el -> el = maxCardCount)
            |> Seq.length


        let sortByType =
            match (jokersCount, maxCardCount, countOfMax) with
            | j, m, _ when (j = 5) && (m = 5) -> 5
            | j, _, _ when (j = 4) -> 5
            | j, _, _ when j = 3 -> if (cardMap.Values.Contains(2)) then 5 else 4
            | j, m, c when j = 2 && m = 2 && c = 2 -> 4
            | j, m, _ when (j = m) -> m + 1
            | j, m, _ -> m + j

        let checkIfFullHouse =
            if
                ((sortByType = 3 && jokersCount = 0 && cardMap.Values.Contains(2))
                 || (sortByType = 3 && jokersCount = 1 && countOfMax = 2))
            then
                1
            else
                0

        let checkIfTwoPairs =
            if (sortByType = 2 && jokersCount = 0 && countOfMax = 2) then
                1
            else
                0


        let sortByFigure =
            hand
            |> List.toArray
            |> Array.map (fun c -> cardsDay2 |> Array.findIndex (fun q -> q = c))

        (sortByType, checkIfFullHouse, checkIfTwoPairs, sortByFigure))

let sum = sumList sortedDay2 0 1

Console.WriteLine(sprintf "%A" sum)
