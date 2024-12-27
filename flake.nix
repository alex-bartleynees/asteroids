{
  description = "A Nix-flake-based Python development environment with pygame";
  inputs.nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.1.*.tar.gz";
  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      devShells = forEachSupportedSystem ({ pkgs }: {
        default = pkgs.mkShell {
          venvDir = ".venv";
          packages = with pkgs; [ 
            python311
            # SDL dependencies for pygame
            SDL2
            SDL2_image
            SDL2_mixer
            SDL2_ttf
          ] ++
            (with pkgs.python311Packages; [
              pip
              venvShellHook
              pygame
              pylint
            ]);
            
          shellHook = ''
            # Create virtual environment if it doesn't exist
            [ -d "$PWD/.venv" ] || python -m venv .venv
            
            # Activate virtual environment
            source .venv/bin/activate
            
            echo "Python virtual environment activated with pygame!"
            echo "Python version: $(python --version)"
            
            # Verify pygame installation
            python -c "import pygame; print(f'Pygame version: {pygame.version.ver}')"
          '';
        };
      });
    };
}
