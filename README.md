# ML Art
This is a repo for creating Machine Learning Generated Art.

## Citations
This pulls/barrows from the following other repositories.
* https://github.com/dvschultz/stylegan2-ada-pytorch

## Scripts
* **SG2_ADA_PyTorch.iphynb**: The PyTorch implamentation of StyleGans. This is the notebook that does the training
* **scrape_google.py**: Scraps images from a google image search
* **scrape_beeple.py**: Scraps images from a beeples daily images
* **image_processing_cut_samples.py**: Takes sample grid output and crops and saves the individual images.
* **image_processing_resize.py**: Resizes a directory of images
* **image_processing_rotate.py**: Rotates abstract images in every way
* **image_processing_window.py**: Takes high resolution images and splits them into multiple images of a specifi size
* **image_tinder.py**: Quickly able to swipe left or right on images to keep
* **image_alpha_check.py**: Checks images for an alpha level

## Datasources
* beeple_210.zip: A collection of Beeple's Everydays (https://www.beeple-crap.com/everydays)

## Backlog
* Make a script for checking how close your image is to the originals

## Article Notes
* Mention of last article
* This is more of a review of other models
    * Helpful ML art class
    * Using styleGAN2 model
        * Talk about the architecture
* Super resolution
    * Target resolution
* Reviewing results
* Printing

## Notes
* 200 Epochs is a good baseline
* Printing
    * Displate does not do custom prints
    * Shutterfly
        * 16x16 Canvis $50 with frame $80
        * 24x36 Canvis $90 with frame $145
        * 36x36 Canvis $110 with frame $180
    * Easycanvisprints - really cheap
    
* Other datasets to try
    * Adobe stock images of abstract
    * Lisa Frank
    * Doctor Sues
    * Bob Ross (https://github.com/jwilber/Bob_Ross_Paintings)
    * Arrival circles (https://github.com/WolframResearch/Arrival-Movie-Live-Coding)
    * Radiohead album cover (not enough images)
    * CT Scans (not enough and not heigh enough resolution)
    * Jack Kirby
* Super resolution repo (https://github.com/alexjc/neural-enhance)
* Just use wifuAI (http://waifu2x.udp.jp/api)

* Next project is the 16:9 Gans
