open System.IO
open System.Text.RegularExpressions
open System

let readLines (filePath: string) =
    seq {
        use sr = new StreamReader(filePath)

        while not sr.EndOfStream do
            yield sr.ReadLine()
    }

let rec calculateValuesAboveDistance (time: int64) (maxTime: int64) (distance: int64) (count: int64) =
    match time with
    | 0L -> count
    | x ->
        let isBetterResult =
            if ((maxTime * x - (int64 (float (x) ** 2))) > distance) then
                1L
            else
                0L

        calculateValuesAboveDistance (time - 1L) maxTime distance (count + isBetterResult)

let rec calculateBetterDistances (times: list<int64>) (distances: list<int64>) (betterDisctancesCounts: list<int64>) =
    match (times, distances) with
    | [], [] -> betterDisctancesCounts
    | t :: tt, d :: dt ->
        let count = calculateValuesAboveDistance t t d 0L
        calculateBetterDistances tt dt (count :: betterDisctancesCounts)
    | _ -> betterDisctancesCounts


let matchesToIntList (matchCollection: MatchCollection) =
    matchCollection
    |> Seq.cast<System.Text.RegularExpressions.Match>
    |> Seq.toList
    |> List.map (fun m -> int64 (m.Value))

let matchNumbers (line: string) = Regex.Matches(line, @"(\d+)")
let dayInput = readLines ("./day-6.txt") |> Seq.toArray
let times = dayInput[0] |> matchNumbers |> matchesToIntList
let distances = dayInput[1] |> matchNumbers |> matchesToIntList

let counts = calculateBetterDistances times distances []
let result = List.fold (fun acc x -> x * acc) 1L counts
Console.WriteLine(sprintf "%A" result)
