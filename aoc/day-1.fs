open System.IO
open System
open System.Text.RegularExpressions

let readLines (filePath: string) =
    seq {
        use sr = new StreamReader(filePath)

        while not sr.EndOfStream do
            yield sr.ReadLine()
    }

let mapToNumber (stringNum: string) =
    match stringNum with
    | "one" -> 1
    | "two" -> 2
    | "three" -> 3
    | "four" -> 4
    | "five" -> 5
    | "six" -> 6
    | "seven" -> 7
    | "eight" -> 8
    | "nine" -> 9
    | _ -> int (stringNum)

let rec sumOfNumbersFromString (sum: int, list: list<string>) =
    let pattern = @"(\d)"
    let numbersAllRegex = @"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

    match list with
    | [] -> sum
    | h :: t ->
        let foundDigits = Regex.Matches(h, pattern)
        let foundStringDigits = Regex.Matches(h, numbersAllRegex)

        // part one:
        // let partialSum =
        //     int (foundDigits[0].Value) * 10 + int (foundDigits[foundDigits.Count - 1].Value)

        // part two:
        let partialSum =
            mapToNumber (foundStringDigits[0].Groups[1].Value) * 10
            + mapToNumber (foundStringDigits[foundStringDigits.Count - 1].Groups[1].Value)

        sumOfNumbersFromString (partialSum + sum, t)



let day1Input = readLines ("./day-1.txt")
let numbersSum = sumOfNumbersFromString (0, Seq.toList (day1Input))
// answer
Console.WriteLine(sprintf "%A" numbersSum)
