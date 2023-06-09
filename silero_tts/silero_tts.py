import sounddevice as sd
import torch

text = "A novel is a long prose narrative that usually describes fictional characters and events in the form of a sequential story. It rests on the consensus that the novel is today the longest genre of narrative prose, followed by the novella, novelette and the short story. However, there is no consensus as to the minimal required lenght. In part because of this wide variation, the boundary between a novella and a novel may be arbitrary and difficult to determine."

language = 'en'
model_id = 'v3_en'
device = torch.device('cpu')

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
model.to(device)

model.speakers

sample_rate = 24000
speaker = 'en_107'
put_accent=True
put_yo=True

model.save_wav(text=text,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        put_yo=put_yo)

audio = model.apply_tts(text=text,
                        speaker=speaker,
                        sample_rate=sample_rate,
                        put_accent=put_accent,
                        put_yo=put_yo)

sd.play(audio, sample_rate)
sd.wait()
