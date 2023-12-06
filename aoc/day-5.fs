open System.IO
open System.Text.RegularExpressions
open System

let readLines (filePath: string) =
    seq {
        use sr = new StreamReader(filePath)

        while not sr.EndOfStream do
            yield sr.ReadLine()
    }

let matchesToIntList (matchCollection: MatchCollection) =
    matchCollection
    |> Seq.cast<System.Text.RegularExpressions.Match>
    |> Seq.toList
    |> List.map (fun m -> int64 (m.Value))

let rec mapToIntList (arr: list<string>) (newArr: list<int64>) =
    match arr with
    | [] -> List.rev newArr
    | h :: t -> mapToIntList t (int64 (h) :: newArr)

let rec getMaps (input: list<string>) (maps: list<list<array<int64>>>) (tempMap: list<array<int64>>) =
    match input with
    | [] -> List.rev ((tempMap |> List.rev) :: maps)
    | h :: t when h = "" -> getMaps t ((tempMap |> List.rev) :: maps) []
    | h :: t when Regex.Matches(h, @"(\d+)").Count = 0 -> getMaps t maps tempMap
    | h :: t ->
        let numbers = matchesToIntList (Regex.Matches(h, @"(\d+)")) |> List.toArray
        getMaps t maps (numbers :: tempMap)

let processSeed (seed: int64) (map: array<array<int64>>) =
    let x =
        Array.tryFind (fun el -> (seed >= Array.get el 1 && seed <= (el[1] + el[2]))) map

    match x with
    | Some s -> seed - s[1] + s[0]
    | None -> seed


let rec processMap (map: array<array<int64>>) (seeds: list<int64>) (pseeds: list<int64>) =
    match seeds with
    | [] -> pseeds
    | h :: t ->
        let pseed = processSeed h map
        processMap map t (pseed :: pseeds)


let rec mapSeeds (seeds: list<int64>) (maps: list<list<array<int64>>>) =
    match maps with
    | [] -> seeds
    | h :: t ->
        let s = processMap (h |> List.toArray) seeds []
        mapSeeds s t

let rec preparePart2Seeds (seeds: list<int64>) (pseeds: list<seq<int64>>) =
    match seeds with
    | [] -> pseeds
    | [ _ ] -> pseeds
    | h :: c :: t ->
        let s =
            seq {
                for i in h .. (h + c) do
                    i
            }

        preparePart2Seeds t (s :: pseeds)

let dayInput = readLines ("./day-5.txt") |> Seq.toArray
let restOfInput = Array.removeManyAt 0 2 dayInput |> Array.toList

let seedsAsStrings =
    Regex.Matches(dayInput[0], @"(\d+)")
    |> Seq.cast<System.Text.RegularExpressions.Match>
    |> Seq.toList
    |> List.map (fun seed -> seed.Value)

let seeds = mapToIntList (seedsAsStrings) []
let newSeeds = preparePart2Seeds seeds []
let maps = getMaps restOfInput [] []

let minx =
    List.fold
        (fun acc x ->
            Console.WriteLine(sprintf "start proccessing: %A" x)

            let k =
                Seq.fold
                    (fun ac2 xx ->
                        let proccessedSeeds = mapSeeds (xx |> Array.toList) maps |> List.min
                        Console.WriteLine(sprintf "proccessed: %A" proccessedSeeds)
                        min ac2 proccessedSeeds)
                    Int64.MaxValue
                    (Seq.chunkBySize 10000000 x)

            Console.WriteLine(sprintf "end: %A" x)
            min k acc)
        Int64.MaxValue
        newSeeds

Console.WriteLine(sprintf "%A" minx)
