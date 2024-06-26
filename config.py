# if needed for remote access, add your stash api_key
api_key = ""
#
# we use the built in plugin access to talk to your stash, this is for search/replacement in URLs
# substitute the replacement for the server url, if they are different
server_url = "http://localhost:9999"
replacement_server_url = "http://localhost:9999"
#
# Where should we save the nfo and playlist files?
# If you put "with files", we will save a .nfo with the video files, named the same, and will make NO playlist file
# Otherwise, put a path here to save into... /home/user/kodistashfiles or C:\kodistashfiles
save_path = "with files"
#
# filenaming options: stashid or filename?  stashid (a number) is cleaner, and sure to be updated (and not orphaned), even if the filename changes.
# if you set the above to "with files", it'll force filename anyway, to match the filename.
filename = "filename"
#
# name of playlist file extension
# choices: strm, or m3u, or m3u8
playlist_ext = "strm"
#
# use extended playlist (extm3u) info?
# This works in Kodi, and ensures the scene name appears in Kodi playlist, otherwise it just says 'stream'
# Use false if you are using some non-Kodi application that doesn't support it, and you just want a pure URL strm file.
m3u = True
#
# name of tag that is parent of Genre tags, so we can label Genres. If set to empty ("") only main tags without children will be used as genre
genre_parentname = ""
#
# When should the nfo be generated?
# Possible overwrite values are:
# - "always": will always create/update the nfo (can be destructive of some nfo content if your existing nfo were not generated by this plugin)
# - "new": will only generate the missing nfo (skip if nfo already exists, generate otherwise)
# - "organized": will generate/overwrite an nfo only the the scene is flagged as "organized"
generate_when = "organized"
#
# if set to true, an existing .nfo file is versioned instead of overwritten 
versioning = True
# if set to true, Poster will be written alongside with the NFO (only works if save path is set to "with files")
saveposter = True
# if set to true, only scenes that have a movie linked will generate an nfo
onlymovie = True