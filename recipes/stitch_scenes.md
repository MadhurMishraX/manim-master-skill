# Stitch Scenes

## Use when

You rendered multiple scene classes and need one final video.

## Create concat.txt

```txt
file 'media/videos/script/480p15/Scene1_Hook.mp4'
file 'media/videos/script/480p15/Scene2_CoreIdea.mp4'
file 'media/videos/script/480p15/Scene3_Conclusion.mp4'
```

## Stitch

```bash
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4
```

## If copy fails

```bash
ffmpeg -y -f concat -safe 0 -i concat.txt -c:v libx264 -pix_fmt yuv420p -c:a aac final.mp4
```

## Common mistakes

- wrong quality folder,
- typo in scene name,
- missing scene render,
- running ffmpeg from wrong directory.
