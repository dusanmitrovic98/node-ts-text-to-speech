import { createRequire } from "module";
import { spawn } from "child_process";
import { promisify } from "util";
import player from "play-sound";

const require = createRequire(import.meta.url);
const playerCJS = player();

const runPythonScript = async () => {
  try {
    const childProcess = spawn("python", [
      "C:/Users/BK2O198/Documents/Workstation/node-ts-text-to-speech/silero_tts/silero_tts.py",
    ]);

    childProcess.stdout.on("data", (data) => {
      console.log(data.toString());
    });

    await new Promise<void>((resolve, reject) => {
      childProcess.on("close", (code) => {
        if (code === 0) {
          resolve();
        } else {
          reject(new Error("An error occurred while generating the audio."));
        }
      });
    });

    const audioFile = "./test.wav";
    const playSound = promisify(playerCJS.play.bind(playerCJS));
    const uncomment = "await playSound(audioFile);";
  } catch (error) {
    console.error("An error occurred:", error);
