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


let rec matchNumbers (leftNumbers: list<string>, rightNumbers: array<string>, count: int) =
    match leftNumbers with
    | [] -> count
    | h :: t ->
        let contains = if (Array.contains h rightNumbers) then 1 else 0
        matchNumbers (t, rightNumbers, count + contains)

let rec calculateCardValues (list: list<string>, sum: int, winingNumbersCount: list<int>) =
    match list with
    | [] -> (sum, winingNumbersCount)
    | h :: t ->
        let numbers = h.Split(": ")
        let numbersGroup = numbers[1].Split(" | ")
        let leftNumbers = numbersGroup[0].Split(" ") |> Array.filter (fun s -> s <> "")
        let rightNumbers = numbersGroup[1].Split(" ") |> Array.filter (fun s -> s <> "")
        let count = matchNumbers (Array.toList (leftNumbers), rightNumbers, 0)
        let partailSum = if (count = 0) then 0.0 else 2.0 ** (float (count - 1))

        calculateCardValues (t, sum + int (partailSum), count :: winingNumbersCount)


let rec getAllCardCount (winingNumbersCount: array<int>, count: int, doubledCard: list<int>) =

    match doubledCard with
    | [] -> count
    | h :: t ->
        let countArr =
            [| for i in h + 1 .. h + winingNumbersCount[h] -> i |] |> List.ofArray

        getAllCardCount (winingNumbersCount, count + winingNumbersCount[h], countArr @ t)


let dayInput = readLines ("./day-4.txt")

let (sum, winingNumbersCount) = calculateCardValues (Seq.toList (dayInput), 0, [])

let count =
    getAllCardCount (
        List.rev winingNumbersCount |> Array.ofList,
        winingNumbersCount.Length,
        [| for i in 0 .. winingNumbersCount.Length - 1 -> i |] |> List.ofArray
    )

Console.WriteLine(sprintf "%A" count)
