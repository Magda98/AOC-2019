open System.IO
open System
open System.Text.RegularExpressions

let readLines (filePath: string) =
    seq {
        use sr = new StreamReader(filePath)

        while not sr.EndOfStream do
            yield sr.ReadLine()
    }

let rec createMap (lines: list<string>) (map: Map<string, string * string>) =
    match lines with
    | [] -> map
    | h :: t ->
        let splited = h.Split(" = ")
        let key = splited[0]
        let values = splited[1].Split(", ")
        let valueLeft = values[0].Trim(([| '(' |]))
        let valueRight = values[1].Trim(([| ')' |]))
        createMap t (map.Add(key, (valueLeft, valueRight)))

let rec calculateSteps
    (steps: list<char>)
    (oSteps: list<char>)
    (currentStepKey: string)
    (map: Map<string, string * string>)
    (stepsCount: int)
    =
    match (steps, currentStepKey) with
    | [], key when Regex.Matches(key, @"(\w\wZ)").Count = 1 -> stepsCount
    | [], _ -> calculateSteps oSteps oSteps currentStepKey map stepsCount
    | h :: t, _ ->
        let (lValue, rValue) =
            match map.TryFind(currentStepKey) with
            | Some v -> v
            | None -> ("", "")

        let nextStep = if (h = 'L') then lValue else rValue
        calculateSteps t oSteps nextStep map (stepsCount + 1)

let dayInput = readLines ("./day-8.txt") |> Seq.toList
let instructions = dayInput.Head.ToCharArray() |> Array.toList
let dayInputArray = dayInput |> List.toArray
let inputGraph = dayInputArray[2..] |> Array.toList

let map = createMap inputGraph Map.empty

let steps = calculateSteps instructions instructions "AAA" map 0

// part 2
let startNodes = [ "FQA"; "JSA"; "GJA"; "PBA"; "AAA"; "NNA" ]
let steps2 = calculateSteps instructions instructions "NNA" map 0
// calculate LCM (least common multiple) for values: 18727, 24253, 18113, 22411, 21797, 16271

Console.WriteLine(sprintf "%A" map)
