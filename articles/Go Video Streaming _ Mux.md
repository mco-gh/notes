Go Video Streaming | Mux

# Video for Go with Mux

Easily build beautiful video experiences into your Go app.

## Installation

### Pull the package

	go get github.com/muxinc/mux-go

## Usage

To start, you'll need a [Mux access token](https://dashboard.mux.com/settings/access-tokens). Once you've got that locally, you're all set!

	package main

	import (
	    "fmt"
	    "os"
	    "github.com/muxinc/mux-go"
	)

	func main() {
	    // API Client Initialization
	    client := muxgo.NewAPIClient(
	        muxgo.NewConfiguration(
	            muxgo.WithBasicAuth(os.Getenv("MUX_TOKEN_ID"), os.Getenv("MUX_TOKEN_SECRET")),
	        ))
	    // Create the Asset
	    asset, err := client.AssetsApi.CreateAsset(muxgo.CreateAssetRequest{
	        Input: []muxgo.InputSettings{
	            muxgo.InputSettings{
	                Url: "https://storage.googleapis.com/muxdemofiles/mux-video-intro.mp4",
	            },
	        },
	        PlaybackPolicy: []muxgo.PlaybackPolicy{muxgo.PUBLIC},
	    })

	    // Check everything was good, and output the playback URL
	    if err == nil {
	        fmt.Printf("Playback URL: https://stream.mux.com/%s.m3u8 \n", asset.Data.PlaybackIds[0].Id)
	    } else {
	        fmt.Printf("Oh no, there was an error: %s \n", err)
	    }
	}

## Video for your Go app that streams beautifully, everywhere

Getting started is fast and easy with direct uploads - this means no intermediate storage for you to manage.

Mux integrates with all major web and mobile video players.

Automatically deliver the best user experience for every combination of device, browser, location, bandwidth, etc.

Also includes helpers for Mux Data if you want to include performance metrics into your own dashboard client.

## Flexible and future-proof

Ingest using almost any codec, including H.264, H.265, VP9, and Apple ProRes. Get multi-bitrate adaptive streaming with HLS delivery.

Adapt to new devices and codecs with no extra work. We’ll automatically update codecs and renditions over the life of a video.

## Security for your video content

Use signed playback policies by easily creating signed URL tokens for your Mux assets when you want to control access to a piece of content.

## Fork it.

We ❤️ issues, pull requests, forks, and compliments (constructive criticism counts too).

[See more at Github](https://github.com/muxinc/mux-go)