import { createRequire } from "module";
import { spawn } from "child_process";
import { promisify } from "util";
import player from "play-sound";

const require = createRequire(import.meta.url);
const playerCJS = player();
