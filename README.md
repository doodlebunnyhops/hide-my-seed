# hide-my-seed
Minecraft PE Resource Pack for hiding your seed on dedicated servers

## Server Prep

1. It is always in your best interest to backup your world(s) before any updates!
1. Once you have created a backup, `stop` your server.

## Download

### Option 1 git clone

1. In your servers path `/home/minecraft-pe/server/worlds/WORLD_NAME/resource_packs` run:
    1. `git clone https://github.com/doodlebunnyhops/hide-my-seed`

### Option 2 download zip

1. Go to https://github.com/doodlebunnyhops/hide-my-seed
1. Select Code
    1. Select `Download ZIP`
    1. Unzip
        1. You may notice the unzip directory looks like: 
        `hide-my-seed-main/hide-my-seed-main/`
        1. Rename the second `hide-my-seed-main` to `hide-my-seed` and use this folder for the next step.
1. Copy the folder into `/home/minecraft-pe/server/worlds/WORLD_NAME/resource_packs`

### Verify Download

Your file structure should now look like this inside your `/home/minecraft-pe/server/worlds/WORLD_NAME/resource_packs` directory:

```text
resource_packs
└── hide-my-seed
    |   LICENSE
    |   manifest.json
    |   pack_icon.png
    |   README.md
    |   world_resource_pack_history.json
    |   world_resource_packs.json
    └── ui
        └── settings_sections
                world_section.json
└── Other Resource Packs...

```


---

## Final Setup

1. If you **do not have** `world_resource_packs.json` or `world_resource_pack_history.json` file in your `/home/minecraft-pe/server/worlds/WORLD_NAME` directory then:
    1. Move those 2 files from `/home/minecraft-pe/server/worlds/WORLD_NAME/resource_packs/hide-my-seed` to `/home/minecraft-pe/server/worlds/WORLD_NAME`
1. If you **already have** `world_resource_packs.json` or `world_resource_pack_history.json` file in your `/home/minecraft-pe/server/worlds/WORLD_NAME` directory then:
    1. copy the contents in each file and add it to their respective files.

### Verify Files

Your file structure should now look like this inside your `/home/minecraft-pe/server/worlds/WORLD_NAME` directory:

```text
WORLD_NAME
|   world_resource_pack_history.json
|   world_resource_packs.json
└───resource_packs
    └── hide-my-seed
        |   LICENSE
        |   manifest.json
        |   pack_icon.png
        |   README.md
        └── ui
            └── settings_sections
                world_section.json
```

## Final Steps

1. Start your server back up
1. Play your minecraft server
1. Go to `settings` in game and under `Game` settings you should no longer see your world seed.
1. Congrats you did it!