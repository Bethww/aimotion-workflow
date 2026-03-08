# Pipeline Deep Dive

## Execution Stages

### 1. Planning
`ScenePlanner` reads a storyboard and produces a `Timeline` — an ordered list of `Scene` objects, each containing `Frame` objects tagged as keyframes.

### 2. Generation
`FrameGenerator` dispatches `GenerationRequest` objects to the configured API adapter for all keyframes. Rate limiting and retries are applied.

### 3. Interpolation
`FrameInterpolator` generates intermediate frames between keyframes. Methods: RIFE (high quality), FILM (large motion), linear (cross-fade fallback).

### 4. Composition
`Compositor` pipes all frames through FFmpeg to produce the final video. Codec, resolution, and FPS are configurable.

## Error Handling
Each stage returns the modified `Timeline`. Partial failures are logged as warnings; a final report summarizes results.
