import React from "react";
import Typeahead from "./Typeahead"
import "./styles.css";

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      storeData: [] ,
      isLoading: true
    };
  }

  componentDidMount(){
    fetch('http://localhost/backend/stores')
      .then(response => response.json())
      .then(data => this.setState({ storeData: data, isLoading: false}));
  }

  render(){
    console.log('this.state 2:', this.state);
    console.log('this.state.storeData', this.state.storeData);
    console.log('this.state.storeData.stores', this.state.storeData.stores);
    const st = this.state.storeData.stores;
    console.log('st: ', st);

    return this.state.isLoading
      ? <p>Loading</p>
      :
      <div>
        <h1>Store Search</h1>
        <Typeahead
          suggestions={st.map(x => x.name)}
        />
      </div>

  }
};

export default App;
