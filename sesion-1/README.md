# Comandos de Git

```bash
# Inicializar un nuevo repositorio
git init

# Agregar todos los archivos en el folder actual:
git add .

# Agregar archivos específicos:
git add <nombre-archivo>

# Crear un commit
# Estamos definiendo una nueva versión con los cambios hechos para agregar al historial:
git commit -m "<descripcion>"

# Vincular repositorio local a repositorio remoto:
git remote add origin <link-repositorio-remoto>

# Sincronizar cambios con repositorio remoto (subir/mandar cambios):
git push -u origin <rama>
```
## Notas

- En cualquier momento pueden verificar el estado actual del repositorio, para ver cuales archivos han cambiado, cuales no están monitoreados por Git ("untracked files"), cuales archivos están "preparados" para un commit y cuales no ("staged" vs. "unstaged" files), etc.

    ```bash
    # Comando para verificar estado de repositorio:
    git status
    ```

- Asegurarse que tu Git local esté configurado con su usuario y correo de tu cuenta de Github:
   - El commit que crean localmente se "firma" con los credenciales configurados.
   - Si esas credenciales no tienen acceso al repositorio remoto, no pueden hacer `git push`.
   - Comandos para configurar credenciales:

       ```bash
       $ git config --global user.name <usuario>
       $ git config --global user.email <email>
       ```

   - Comando para verificar configuración local:
       ```bash
       git config --global --list
       ```

- Si su repositorio local no está sincronizado con el remoto, no pueden hacer push.
   - Comando para sincronizar cambios remotos en un repositorio local:
       ```bash
       git pull
       ```
