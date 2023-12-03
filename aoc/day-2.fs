open System.IO
open System.Text.RegularExpressions
open System

let readLines (filePath: string) =
    seq {
        use sr = new StreamReader(filePath)

        while not sr.EndOfStream do
            yield sr.ReadLine()
    }

let getNumber (line: string) =
    let matchedNumber = Regex.Matches(line, @"(\d+)")
    int (matchedNumber[0].Value)

let rec calculateIfPossible (g: list<string>, isPossible: bool) =
    match g with
    | [] -> isPossible
    | h :: t ->
        let b = Regex.Matches(h, @"(\d+ blue)")
        let r = Regex.Matches(h, @"(\d+ red)")
        let g = Regex.Matches(h, @"(\d+ green)")
        let isBluePossible = if (b.Count > 0) then getNumber (b[0].Value) <= 14 else true
        let isRedPossible = if (r.Count > 0) then getNumber (r[0].Value) <= 12 else true
        let isGreenPossible = if (g.Count > 0) then getNumber (g[0].Value) <= 13 else true
        calculateIfPossible (t, isPossible && isBluePossible && isRedPossible && isGreenPossible)


let rec calculateMaxPossible (g: list<string>, rMax: int, gMax: int, bMax: int) =
    match g with
    | [] -> [ rMax, gMax, bMax ]
    | h :: t ->
        let b = Regex.Matches(h, @"(\d+ blue)")
        let r = Regex.Matches(h, @"(\d+ red)")
        let g = Regex.Matches(h, @"(\d+ green)")
        let blueNumber = if (b.Count > 0) then getNumber (b[0].Value) else 0
        let redNumber = if (r.Count > 0) then getNumber (r[0].Value) else 0
        let greenNumber = if (g.Count > 0) then getNumber (g[0].Value) else 0
        let newBlueMax = if (blueNumber > bMax) then blueNumber else bMax
        let newGreenMax = if (greenNumber > gMax) then greenNumber else gMax
        let newRedMax = if (redNumber > rMax) then redNumber else rMax
        calculateMaxPossible (t, newRedMax, newGreenMax, newBlueMax)


let rec calculateGames (lines: list<string>, idsSum, id: int) =
    match lines with
    | [] -> idsSum
    | h :: t ->
        let games = Array.toList (h.Split("; "))
        // let partialSum = if (calculateIfPossible (games, true)) then id else 0
        let [ r, g, b ] = calculateMaxPossible (games, 1, 1, 1)
        let partialSum = r * g * b
        calculateGames (t, idsSum + partialSum, id + 1)





let day = readLines ("./day-2.txt")
let idsSum = calculateGames (Seq.toList (day), 0, 1)
Console.WriteLine(sprintf "%A" idsSum)
