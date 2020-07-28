/*
Este é o arquivo que renderiza as imagens usando
Three.js.

FIXME: quando se troca de panoramica 5 vezes,
tudo fica lento e zoado, provavelmente é poque 
existe mais de Scene sendo criada e destruida

em vez de criar uma nova Scene, o destroy poderia
ser apenas uma forma de diminuir a opacidade pra 0,
 assim não precisaria carregar tantos objetos
*/
import "./styles.css";
import * as THREE from "three";
var OrbitControls = require('three-orbit-controls')(THREE)

import pano1 from './assets/teste2.jpeg'; // Essa é a ultima imagem retornada dos scripts python
import pano2 from './assets/teste1.jpeg'

import feet from './assets/feet.svg'
import { Vector3, Sprite } from "three";
import { TweenLite } from "gsap/gsap-core";


const container = document.body;
const rayCaster = new THREE.Raycaster()

var camera, scene, renderer, controls;


class Scene{

  constructor(image, camera){
    this.image = image
    this.points = []
    this.sprites = []
    this.scene = null

    this.camera = camera
  }

  createScene(scene){
    this.scene = scene
    console.log('Scene created')
    console.log(scene)
    var geometry = new THREE.SphereGeometry(50,32,42); 
  
    var texture = new THREE.TextureLoader().load(this.image);
    texture.wrapS = THREE.RepeatWrapping //Espelhando a imagem
    texture.repeat.x = -1
  
    const material = new THREE.MeshBasicMaterial( { map: texture, side: THREE.DoubleSide, transparent: false } );
    this.material = material
    this.sphere = new THREE.Mesh(geometry,material); //definindo o objeto sendo da forma de "geometry", e do material de "material"
    this.scene.add( this.sphere );

    this.points.forEach(this.addTooltip.bind(this))
  }

  addPoint(point){
    this.points.push(point)
  }

  addTooltip(point){
    let spriteMap = new THREE.TextureLoader().load(feet);
    let spriteMaterial = new THREE.SpriteMaterial( {map: spriteMap} );
    let sprite = new THREE.Sprite( spriteMaterial ); 
    sprite.name = name;
    sprite.position.copy(point.position.clone().normalize().multiplyScalar(30))

    sprite.scale.multiplyScalar(3)

    this.scene.add( sprite );
    this.sprites.push(sprite)

    sprite.onClick = () => {

      this.destroy()
      point.scene.createScene(scene)
      point.scene.appear()
  
    }

    
  }

  destroy(){
    TweenLite.to(this.camera,1,{
      zoom: 2,
      onUpdate: () => {
        this.camera.updateProjectionMatrix()
      }
      
    })
    TweenLite.to(this.sphere.material,1,{
      opacity: 0,
      onComplete: () => {
        this.scene.remove(this.sphere) //sphere
        console.log('panoramica destruida')
      }
    })
    
    this.sprites.forEach((sprite) => {
      TweenLite.to(sprite.scale,0.5,{
        x: 0,
        y: 0,
        z: 0,   
      })
    })
  }

  appear(){
    TweenLite.to(this.camera,0.5,{
      zoom: 1,
      onUpdate: () => {
        this.camera.updateProjectionMatrix()
      }
    }).delay(0.5)
    
    this.sphere.material.opacity = 0;
    TweenLite.to(this.sphere.material,1,{
      opacity: 1
    })

    this.sprites.forEach((sprite) => {
      sprite.scale.set(0,0,0)
      TweenLite.to(sprite.scale,1,{
        x: 2,
        y: 2,
        z: 2,
      })
    })
  }

}

init();
animate();


function init() {
  

  scene = new THREE.Scene();
  render();
  cameraInit()

    
  //SPHEREs
  let s1 = new Scene(pano1, camera)
  let s2 = new Scene(pano2, camera)

  //Adicionando os pontos
  s1.addPoint({
    position: new Vector3(
      43.071192785453675, //Y
      -0.7644674190358015, //X
      24.916103487018965 //z
    ),
    name: 'Corredor',
    scene: s2

  })
  s2.addPoint({
    position: new Vector3(
      -43.071192785453675, //Y
      0.7644674190358015, //X
      -24.916103487018965 //z
    ),
    name: 'cozinha',
    scene: s1

  })

  s1.createScene(scene)
  s1.appear()


  //Redimencionamento da tela
  window.addEventListener( 'resize', onWindowResize, false );
  
  //Mudança do mouse ao mover a camera
  window.onmousedown = () => {container.style.cursor = "move";}
  window.onmouseup = () => {container.style.cursor = "pointer";}
  
  container.addEventListener('click',onclick)
  container.addEventListener('mousemove',onMouseMove)

  //RENDER
  function render(){
    renderer = new THREE.WebGLRenderer();
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );
    container.appendChild( renderer.domElement );
  }

  //CAMERA
  function cameraInit(){

    camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 1000 );
    camera.position.set(1,0,0);
    
    controls = new OrbitControls( camera, renderer.domElement );
    controls.minDistance = 0
    controls.maxDistance = 15.0
  }

  //Função de detecção de click
  function onclick(e){
   
    let mouse  = new THREE.Vector2(
      (e.clientX / window.innerWidth) * 2 - 1,
      - (e.clientY / window.innerHeight) * 2 + 1
    );
    
    rayCaster.setFromCamera(mouse,camera)
    let intersects = rayCaster.intersectObjects(scene.children)
    
    intersects.forEach((intersect) =>{
      if(intersect.object.type == 'Sprite'){
   

        intersect.object.onClick()
      }
    })
    
  }
  function onMouseMove(e){
   
    let mouse  = new THREE.Vector2(
      (e.clientX / window.innerWidth) * 2 - 1,
      - (e.clientY / window.innerHeight) * 2 + 1
    );
  
    
    rayCaster.setFromCamera(mouse,camera)
    let intersects = rayCaster.intersectObjects(scene.children)
    
    intersects.forEach((intersect) =>{
      if(intersect.object.type == 'Sprite'){
        console.log('hover')
      }
        
    })
    
  }

}

function animate() {

  requestAnimationFrame( animate );
	renderer.render( scene, camera );
  controls.update();
}

function toggleFullScreen() {
    if ((document.fullScreenElement && document.fullScreenElement !== null) ||    
      (!document.mozFullScreen && !document.webkitIsFullScreen)){
          
      if (document.documentElement.requestFullScreen) {  
        document.documentElement.requestFullScreen();  
      } 
      
      else if (document.documentElement.mozRequestFullScreen) {  
        document.documentElement.mozRequestFullScreen();  
      } 
      else if (document.documentElement.webkitRequestFullScreen) {  
        document.documentElement.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);  
      }  
    } 
    else {  
      if (document.cancelFullScreen) {  
        document.cancelFullScreen();  
      } else if (document.mozCancelFullScreen) {  
        document.mozCancelFullScreen();  
      } else if (document.webkitCancelFullScreen) {  
        document.webkitCancelFullScreen();  
      }  
    }  
}

function onWindowResize() {
    
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();

  renderer.setSize( window.innerWidth, window.innerHeight );

}
