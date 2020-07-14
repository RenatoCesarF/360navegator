import "./styles.css";
import * as THREE from "three";
var OrbitControls = require('three-orbit-controls')(THREE)

import pano from './assets/outraPan.png';

var camera, scene, renderer, controls;

//TODO: arrumar as distorções do canto do navegador

init();
animate();

function init() {

    camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 1000 );
    camera.position.set(1,0,0);


    scene = new THREE.Scene();
//
    //Configurando a esfera e adicionando-a à cena
    var geometry = new THREE.CylinderGeometry(30,30,45,500,200,true); //Formato do objeto

    // Imagem original: https://live.staticflickr.com/65535/50091270432_dd1da38ee7_5k.jpg
    var texture = new THREE.TextureLoader().load( 'https://live.staticflickr.com/65535/50091270432_dd1da38ee7_5k.jpg' );
    var material = new THREE.MeshBasicMaterial( { map: texture, side: THREE.DoubleSide } );
    const sphere = new THREE.Mesh(geometry,material); //definindo o objeto sendo da forma de "geometry", e do material de "material"
    scene.add( sphere );


    //RENDER
    renderer = new THREE.WebGLRenderer();
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );

    
    //CAMERA
    controls = new OrbitControls( camera, renderer.domElement );
    controls.minDistance = 0
    controls.maxDistance = 15.0
    

    //Redimencionamento da tela
    window.addEventListener( 'resize', onWindowResize, false );
    
    //Mudança do mouse ao mover a camera
    window.onmousedown = () => {document.body.style.cursor = "move";}
    window.onmouseup = () => {document.body.style.cursor = "pointer";}
}

function onWindowResize() {
    
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );

}

function animate() {

    requestAnimationFrame( animate );
	renderer.render( scene, camera );
    controls.update();
}