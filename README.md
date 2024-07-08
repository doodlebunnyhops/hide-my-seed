# hide-my-seed
Minecraft PE Resource Pack for hiding your seed on dedicated servers

## Server Prep

1. It is always in your best interest to backup your world(s) before any updates!
1. Once you have created a backup, `stop` your server.

## Download zip

1. Go to [Actions](https://github.com/doodlebunnyhops/hide-my-seed/actions)
    1. Find the most recent run called `Package MCPACK HideMySeed `
1. Download the Artifact `HideMySeed`
    1. Click on `HideMySeed` under the artifact section to download.
    1. Unzip
        1. You will see 2 files.
            - This ReadME
            - HideMySeed.mcpack
          
## Install on your local machine

1. Install the HideMySeed.mcpack resource.
    1. Double click `HideMySeed.mcpack` to install.
    2. Once Minecraft Launcher has signified the install is successful proceed.
1. On your local machine
    1. Create a temp world, it will make it easier to give it a unique name for a later step. Make sure to activate HideMySeed with this temp world.
    3. Open the temp world momentarily then save and exit. This is to generate some files to transfer later.
    4. Migrate to your minecraft world saves, generally in
       
       *Modify USERNAME with your path or possibly different install location.*
        ```
        C:\Users\USERNAME\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds
        ```
        1. Select the world you just created, if you're unsure which one you can open the `levelname.txt` file to see if it's the one you uniquely named earlier.
        2. Keep this folder path handy, you will need it for transfering some files/folders.
  

## Install on Dedicated Server

1. From your local copy folder
   
    ```text
    C:\Users\USERNAME\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds\WORLD_HASH\resource_packs\HideMySeed
    ```
    into
    ```text
    /home/minecraft-pe/server/worlds/WORLD_NAME/resource_packs/HideMySeed
    ```
    
   *Modify USERNAME and WORLD_HASH and WORLD_NAME with your path or possibly different install location.*


### Verify Download

Your file structure should now look like this inside your `/home/minecraft-pe/server/worlds/WORLD_NAME/resource_packs` directory:

```text
resource_packs
└── hide-my-seed
    |   manifest.json
    |   pack_icon.png
    └── ui
        └── settings_sections
                world_section.json
└── Other Resource Packs...

```


---

## Final Setup

1. If you **do not have** `world_resource_packs.json` or `world_resource_pack_history.json` file in your `/home/minecraft-pe/server/worlds/WORLD_NAME` directory then:
    1. Move those 2 files from Local: `C:\Users\USERNAME\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds\WORLD_HASH` to Dedicated: `/home/minecraft-pe/server/worlds/WORLD_NAME`
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
