import { Telegraf } from 'telegraf'
import { createReadStream } from 'fs'
import 'dotenv/config'

var chatId = "-1001537133913"
let token = process.env.TELEGRAM_TOKEN
let args = process.argv.slice(2)
let bot = new Telegraf(token)

let type = args[0]
let src = args[1]

if (type == "m") {

    console.log("Sending Message ...")
    bot.telegram.sendMessage(chatId, src)

} else if (type == "v") {

    const readStream = createReadStream(src)

    bot.telegram.sendVideo(chatId, {
        source: readStream
    })


} else if (type == "p") {

    const readStream = createReadStream(src)

    bot.telegram.sendVideo(chatId, {
        source: readStream
    })

} else {
    bot.telegram.sendMessage("ok")
}
